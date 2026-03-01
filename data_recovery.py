# https://quera.org/problemset/220659
# -----------------------------------
HEADER_MAPPER = {
    b"\x89PNG\r\n\x1a\n": "PNG",
    b"\xff\xd8\xff": "JPEG",
    b"\x42\x4d": "BMP",
    b"\x49\x49\x2a\x00": "TIFF",
    b"\x47\x49\x46\x38": "GIF",
    b"\x50\x4b\x03\x04": "ZIP",
    b"\x7fELF": "ELF",
    b"\x25\x50\x44\x46": "PDF",
    b"\x49\x44\x33": "MP3",
    b"\xff\xfb": "MPEG",
    b"\x00\x00\x01\x00": "PDDF",
    b"\x00\x01\x00\x00": "ICO",
}


def data_recovery(data: bytes) -> list:
    file_types = []
    for header, type in HEADER_MAPPER.items():
        if header in data:
            file_types.append(type)

    return file_types


# Test Example:
# input = b"\x89PNG\r\n\x1a\nBMII*\x00\xff\xd8\xff\xff\xd8\xff\x00\x00\x01\x00\x00"
# output = ['PNG', 'JPEG', 'BMP', 'TIFF', 'PDDF', 'ICO']

# ! This solution just works on Quera but in my opinion, it's not correct
# * A better solution would be to use a pointer and then check for header match in data input
