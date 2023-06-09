from django.shortcuts import render
import os
import json
import plotly.graph_objects as go
import pandas as pd

def graph_view(request):
    current_dir_path = os.getcwd()
    # parent_dir_path = os.path.dirname(current_dir_path)
    target_dir_path = os.path.join(current_dir_path, 'dataapp')
    target_file_path = os.path.join(target_dir_path, 'django_packages_page_data.json')

    with open(target_file_path, 'r', encoding='utf-8') as file:
        packages_data = json.load(file)

    df = pd.json_normalize(packages_data, record_path=list(packages_data.keys())[0])
    df['package_id'] = list(packages_data.keys())[0]
    for k in list(packages_data.keys())[1:]:
        df_temp = pd.json_normalize(packages_data, record_path=k)
        df_temp['package_id'] = k
        df = pd.concat([df, df_temp], ignore_index=True)


    # django_packages.json to df_

    target_file_path = os.path.join(target_dir_path, 'django_packages.json')

    with open(target_file_path, 'r', encoding='utf-8') as file:
        packages_data = json.load(file)

    categories = []
    packages = []
    repo_links = []
    links = []
    ids = []

    for category_name, category_data in packages_data.items():
        category_description = category_data['category_description']
        for package_data in category_data['packages']:
            package_name = package_data['package_name']
            repository_link = package_data['repository_link']
            link = package_data['link']
            package_id = package_data['id']
            categories.append(category_name)
            packages.append(package_name)
            repo_links.append(repository_link)
            links.append(link)
            ids.append(package_id)

    df_ = pd.DataFrame({
        'category_name': categories,
        'category_description': [category_data['category_description'] for category_data in packages_data.values() for package_data in category_data['packages']],
        'package_name': packages,
        'repository_link': repo_links,
        'link': links,
        'id': ids
    })


    # Filter data to keep packages with GitHub repository, without Alert Status. 
    mask_git = df['repository_link'].str.strip().str.contains('https://github.com')
    mask_alert = df['alert'].str.contains('No Alert')
    df = df[['id', 'package_name','stars','forks','description', 'alert', 'alert_date', 'repository_link', 'documentation_link', 'pypi_link', 'current_version', 'license', 'last_release', 'releases_num', 'diff_between_last_and_first_releases', 'avg_days_between_releases', 'status', 'python_3']]
    df_filtered = df[mask_git]
    df_filtered = df_filtered[mask_alert]

    merged_df = pd.merge(df_filtered,df_[['id', 'category_name', 'link']], on="id")

    # Remove duplicates 
    merged_df = merged_df.drop_duplicates(subset='repository_link')

    merged_df=merged_df[['package_name', 'stars', 'forks']]

    merged_df['stars'] = pd.to_numeric(merged_df['stars'], errors='coerce',downcast="integer") 
    merged_df['forks'] = pd.to_numeric(merged_df['forks'], errors='coerce',downcast="integer")
    

    df_sorted_stars = merged_df.sort_values('stars', ascending=False)
    top_10 = df_sorted_stars.head(10)
    fig1 = go.Figure(data=[go.Bar(x=top_10['package_name'], y=top_10['stars'])])
    # graph_html1 = fig1.to_html(full_html=False, default_height=500, default_width=700)

    df_sorted_forks = merged_df.sort_values('forks', ascending=False)
    top_10 = df_sorted_forks.head(10)
    fig2 = go.Figure(data=[go.Bar(x=top_10['package_name'], y=top_10['forks'])])
    # graph_html2 = fig2.to_html(full_html=False, default_height=500, default_width=700)
    fig1_json = fig1.to_json()
    fig2_json = fig2.to_json()
    context = {'fig1_json': fig1_json, 'fig2_json': fig2_json}
    # context = {'graph_html1': graph_html1, 'graph_html2': graph_html2}
    return render(request, 'base.html', context)
