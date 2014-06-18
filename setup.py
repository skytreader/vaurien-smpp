from distutils.core import setup

setup(
    name = "vaurienex-smpp",
    version = "0.1.0",
    author = "Chad Estioco",
    author_email = "chadestioco@gmail.com",
    url = "https://github.com/skytreader/vaurien-smpp",
    packages = ["vaurien.smpp",],
    install_requires = ["vaurien", "smpp.pdu"],
    license="MIT",
    description = "SMPP extension for Vaurien.",
)
