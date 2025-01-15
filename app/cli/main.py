import typer
from app.creator.files_creator import create_project_structure, package_installer
main_app = typer.Typer()


@main_app.command(name='create')
def create_ds(project_name: str):
    create_project_structure(project_name)
    package_installer(project_name)


@main_app.command(name="hey")
def hello(name: str):
    typer.echo(f"Hello my dear {name}")


if __name__ == "__main__":
    main_app()
