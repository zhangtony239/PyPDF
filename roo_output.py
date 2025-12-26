from pypdf import PdfReader, PdfWriter

# 1. 获取 data.pdf 的页面尺寸
data_reader = PdfReader("data.pdf")
first_data_page = data_reader.pages[0]
target_width = first_data_page.mediabox.width
target_height = first_data_page.mediabox.height

# 2. 创建一个 PdfWriter 实例
writer = PdfWriter()

# 3. 读取并处理 cover.pdf
cover_reader = PdfReader("cover.pdf")
for page in cover_reader.pages:
    # 缩放 cover.pdf 的页面以匹配 data.pdf 的尺寸
    page.scale_to(width=target_width, height=target_height)
    # 添加缩放后的页面
    writer.add_page(page)

# 4. 追加 data.pdf
writer.append("data.pdf")

# 5. 写入输出文件
with open("merged-pdf.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("PDFs have been merged into merged-pdf.pdf, with cover pages resized.")