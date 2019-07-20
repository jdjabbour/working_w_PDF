import tabula

# Reads the PDF
df = tabula.read_pdf("Employee Summary.pdf", multiple_tables=True)

#data2 = tabula.read_pdf("VN2p_2012.pdf", output_format="json")

print df

tabula.convert_into("Employee Summary.pdf", "offense_testing.xlsx", output_format="xlsx")