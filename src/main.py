import PyPDF2, os, fitz
# 发票处理
# 餐票 -> 姓名+金额+日期
# 打车票（行程单+发票）
pdf_file_folders = '~/Desktop/tmp/'


# 打开PDF文件
pdf_document = 'path/to/your/pdf_file.pdf'
# 将路径转换为绝对路径
pdf_file_folders = os.path.expanduser(pdf_file_folders)


# 遍历目录中的所有文件
for root, dirs, files in os.walk(pdf_file_folders):
    for file in files:
        if file.endswith('.pdf'):
            pdf_document = os.path.join(root, file)
            doc = fitz.open(pdf_document)

            # 遍历每一页
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()
                print(f"File: {pdf_document}, Page: {page_num + 1}")
                print(text)