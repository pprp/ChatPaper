from review.get_paper_from_pdf import Paper 

def test_get_paper_from_pdf():
    paper = Paper('./tests/TEST_NAS1.pdf')

    # teset get_image_path 
    # print(paper.get_image_path(image_path='./images'))

    # # test get_chapter_names
    # print(paper.get_chapter_names())

    # test get_all page
    print(paper._get_all_page())

if __name__ == "__main__":
    test_get_paper_from_pdf()