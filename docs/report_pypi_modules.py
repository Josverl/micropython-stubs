import pandas as pd
import jinja2 as j2

template_env = j2.Environment(loader=j2.FileSystemLoader("./templates"))


def create_md():
    # create a template environment

    df = pd.read_json("../all_modules.json")
    # remove the mod_name and pkg_version columns
    df = df.drop(columns=["mod_name", "pkg_version", "hash", "family"])
    # keep only unique rows
    df = df.drop_duplicates()

    # filter out the highest version
    df_pypi = df[df["version"] != df["version"].max()]
    df_git = df[df["version"] == df["version"].max()]

    report_to_md(df_pypi, "modules_pypi.md.j2", "modules_pypi_body.md")
    # only the (latests) preview version
    report_to_md(df_git, "modules_git.md.j2", "modules_git_body.md")


def report_to_md(df_pypi, template, dest_md):
    # load the template file
    template = template_env.get_template(template)
    grouped = df_pypi.groupby("version")

    # create a list to store the rendered modules
    rendered_modules = []

    # iterate over each group in the grouped dataframe
    for version, group in grouped:
        # render the template with the group data
        rendered_module = template.render(version=version, modules=group.to_dict(orient="records"))
        # append the rendered module to the list
        rendered_modules.insert(0, rendered_module)

    # join the rendered modules into a single string
    rendered_modules_str = "\n".join(rendered_modules)

    # save to docs/published_body.md
    with open(dest_md, "w") as file:
        file.write(rendered_modules_str)
