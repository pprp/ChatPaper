from scipdf.pdf.parse_pdf import parse_pdf_to_dict

article_dict = scipdf.parse_pdf_to_dict('https://www.biorxiv.org/content/biorxiv/early/2018/11/20/463760.full.pdf', as_list=False)
print(article_dict)
