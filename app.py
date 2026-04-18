from io import BytesIO
import qrcode as qr
import streamlit as st

# SIDEBAR
with st.sidebar:
    st.subheader("⚙️ Customize QR")

    fill_color = st.color_picker("QR Color", "#000000")
    back_color = st.color_picker("Background Color", "#FFFFFF")

    box_size = st.slider("QR Size", 5, 15, 10)
    #logo_file = st.file_uploader("Upload Logo (optional)", type=["png", "jpg"])

    st.markdown("---")

    st.subheader("ℹ️ About this app")
    st.write("👨‍💻 Created by **Dip Mondal**")
    
    st.markdown("---")
    st.markdown("### 📌 How to use")
    st.markdown("""
    1. Enter text or URL  
    2. Click **Generate QR Code**  
    3. Download the QR image  
    """)
    st.markdown("---")
    st.info("💡 You can use this QR for websites, text, or sharing links.")

# main app
st.title('📱 QR Generator')
st.write("Generate QR codes from text or URL")
url=st.text_input('Enter text')

name=st.text_input('Enter filename ','Qr.png')

if st.button("Generate"):
    if url:
        img = qr.QRCode(

            version=None,
            box_size=box_size,
            border=4,
        )
        img.add_data(url)
        img.make(fit=True)

        img = img.make_image(fill_color=fill_color, back_color=back_color)
        
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)
        st.image(buf.getvalue(),width=300)

        st.download_button(
            label="Download QR",
            data=buf.getvalue(),
            file_name=name if name.endswith('.png') else name + '.png',
            mime="image/png"
        )

    else:
        st.warning("Please enter some text")

