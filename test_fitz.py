import fitz
import pdb

cand_list = [
    "./tests/TEST_NAS1.pdf",
    "./tests/TEST_NAS2.pdf",
    "./tests/TEST_NAS3.pdf",
    "./tests/TEST_NAS4.pdf",
    "./tests/TEST_NAS5.pdf",
    "./tests/TEST_NAS6.pdf",
    "./tests/TEST_NAS7.pdf",
    "./tests/TEST_NAS8.pdf",
    "./tests/TEST_NAS9.pdf",
]


def find_abstract(text):
    # return index
    idx = text.find("Abstract")
    if idx == -1:
        idx = text.find("a b s t r a c t")
    if idx == -1:
        idx = text.find("ABSTRACT")
    if idx == -1:
        idx = text.find("Ab s tract")
    if idx == -1:
        idx = text.find("A b s t r a c t")
    if idx == -1:
        idx = text.find("A B S T R A C T")
    if idx == -1:
        idx = text.find("AbStRaCt")
    return idx


def find_introduction(text):
    idx = text.find("Introduction")
    if idx == -1:
        idx = text.find("INTRODUCTION")
    if idx == -1:
        idx = text.find("introduction")       
    return idx


def find_related_work(text):
    idx = text.find("Related Work")
    if idx == -1:
        idx = text.find("RELATED WORK")
    if idx == -1:
        idx = text.find("related work")
    return idx


def find_experiments(text):
    """with no number"""
    idx = text.find("Experiments")
    if idx == -1:
        idx = text.find("EXPERIMENTS")
    if idx == -1:
        idx = text.find("experiments")
    if idx == -1:
        idx = text.find("Experiment")
    if idx == -1:
        idx = text.find("EXPERIMENT")
    if idx == -1:
        idx = text.find("experiment")
    return idx


def find_end_of_paper(text):
    """with no number"""
    idx = text.find("References")
    if idx == -1:
        idx = text.find("REFERENCES")
    if idx == -1:
        idx = text.find("references")
    if idx == -1:
        idx = text.find("Bibliography")
    if idx == -1:
        idx = text.find("BIBLIOGRAPHY")
    if idx == -1:
        idx = text.find("bibliography")
    if idx == -1:
        idx = text.find("Acknowledgments")
    if idx == -1:
        idx = text.find("ACKNOWLEDGMENTS")
    if idx == -1:
        idx = text.find("acknowledgments")
    if idx == -1:
        idx = text.find("Acknowledgment")
    if idx == -1:
        idx = text.find("ACKNOWLEDGMENT")
    if idx == -1:
        idx = text.find("acknowledgment")
    if idx == -1:
        idx = text.find("Acknowledgement")
    return idx


def find_conclusion(text):
    idx = text.find("Conclusion")
    if idx == -1:
        idx = text.find("CONCLUSION")
    if idx == -1:
        idx = text.find("conclusion")
    return idx


def strip_end_of_line(text):
    """strip \n and combine into one line"""
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    return text


def test_get_title():
    # extract the title
    """
    Extract the title of the following paragraph: {content} Answer me with the title only.
    """
    for cand in cand_list:
        doc = fitz.open(cand)
        page = doc.load_page(0)
        text = page.get_text("text")
        print(cand)
        print(strip_end_of_line(text[:300]))
        print("*" * 40)

def test_get_abstract():
    """
    usually on the first page.
    Extract the abstract of the following paragraph: {content} Answer me with the abstract only.
    """
    for cand in cand_list:
        print(cand)
        doc = fitz.open(cand)
        page = doc.load_page(0)
        text = page.get_text("text")
        # extract the texts from "Abstract" or "a b s t r a c t" to "1\n Introduction" in text
        start = find_abstract(text)
        end = find_introduction(text)

        if start == -1 or end == -1:
            print("No abstract found!")
        else:
            abstract = text[start:end]
            print(strip_end_of_line(abstract))
        print("*" * 40)


def test_get_introduction():
    """
    Usually on the first or second page.
    First concate the contents of the first two pages, then extract the texts from "1\n Introduction" to "2\n Related Work" in text
    """
    for cand in cand_list:
        print(" * ", cand)
        doc = fitz.open(cand)
        page1 = doc.load_page(0)
        text1 = page1.get_text("text")
        page2 = doc.load_page(1)
        text2 = page2.get_text("text")
        page3 = doc.load_page(2)
        text3 = page3.get_text("text")
        text = text1 + text2 + text3
        # extract the texts from "introduction" or "a b s t r a c t" to "1\n Introduction" in text
        start = find_introduction(text)
        end = find_related_work(text)

        # print(f" * DEBUG: start={start}, end={end}")
        if end == -1:
            end = start + 3000 # max
        if start == -1 or end == -1:
            print("No introduction found!")
        else:
            if end > start + 3000:
                end = start + 3000
            introduction = text[start:end]
            print(strip_end_of_line(introduction))
        print("*" * 40)


def test_get_conclusion():
    """Usually on the last page."""
    for cand in cand_list:
        print(" * ", cand)
        doc = fitz.open(cand)
        text = "".join(page.get_text("text") for page in doc)
        # extract the texts from "conclusion" or "a b s t r a c t" to "1\n Introduction" in text
        start = find_conclusion(text)
        end = find_end_of_paper(text)

        if end == -1:
            # set the max length of conclusion
            end = start + 1000  # max

        if start == -1 or end == -1:
            print("No conclusion found!")
        else:
            print(f" * start: {start}, end: {end}")
            if end > start + 1000:
                end = start + 1000
            conclusion = text[start:end]
            print(strip_end_of_line(conclusion))

        print("*" * 40)


if __name__ == "__main__":
    test_get_abstract()
    test_get_introduction()
    # test_get_title()
    # test_get_conclusion()
