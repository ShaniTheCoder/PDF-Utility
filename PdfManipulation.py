from PyPDF2 import PdfReader, PdfWriter


def EncryptPdf(password):
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open("encryptedCert.pdf", 'wb') as f:
        writer.write(f)


def DecryptPdf(password, pdfFile):
    reader = PdfReader(pdfFile)
    writer = PdfWriter()
    if reader.is_encrypted:
        reader.decrypt(password)
    for page in reader.pages:
        writer.add_page(page)
    with open("decrypted.pdf", 'wb') as file:
        writer.write(file)


def ExtractText():
    if len(reader.pages) > 1:
        for page in reader.page:
            # with open()
            page.extract_text()
    page = reader.pages[0]
    with open(f"extracted{reader.metadata.title}.txt", 'w') as file:
        file.write(page.extract_text())


def AddMetadata(title, author,  creator, pseudoTitle):
    # todo: add a warning that file will be saved with the title of pdf which is different than the file name and can be none so enter a suitable title or the file will be saved as none.pdf
    if title == None:
        title = pseudoTitle

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": author,
            "/Creator": creator,
            "/Producer": "Pdf-Utility(by ShaniTheCoder(github))"

        }
    )
    with open("meta-pdf.pdf", "wb") as f:
        writer.write(f)


def ImageToPdf():
    from PIL import Image

    images = [
        Image.open("C:/Users/91992/Desktop/Projects/Pdf-Utility/sample/" + f)
        for f in ["sample1.jpeg", "sample2.jpeg", "sample3.jpeg"]
    ]

    pdf_path = "C:/Users/91992/Desktop/Projects/Pdf-Utility/sample/imageJpeg.pdf"

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


def MergePdf(*pdFile):
    merger = PdfWriter()

    for pdf in pdFile:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()


if __name__ == '__main__':
    file = r"sample\IndependenceCert.pdf"
    MergePdf("sample\decrypted.pdf",
             "sample\imageJpeg.pdf", "sample\IndependenceCert.pdf")
