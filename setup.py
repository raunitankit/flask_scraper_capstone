from setuptools import setup, find_packages

setup(
    name="flask_scraper_capstone",
    version="0.1",
    packages=find_packages(),
    install_requires=["flask", "requests", "beautifulsoup4", "pandas"],
    entry_points={
        "console_scripts": [
            "scraper-dashboard=app:app.run"
        ]
    },
)