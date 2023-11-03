resource(name="setup_desk", source="setup_desk.py")
python_distribution(
    name="desk",
    dependencies=[
    ":setup_desk",
    "src/python/apps/desk"
    ],
    provides=setup_py(
        name="desk-dist",
        version="1.0",
    ),
    generate_setup = False
)
python_distribution(
    name="mobile",
    dependencies=[
    "src/python/apps/mobile"
    ],
    provides=python_artifact(
        name="mobile-dist",
        version="1.0"
    ),
    generate_setup = False
)