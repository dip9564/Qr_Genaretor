from io import BytesIO
import qrcode as qr
import streamlit as st
from PIL import Image, ImageDraw

# SIDEBAR
with st.sidebar:
    st.subheader("⚙️ Customize QR")

    fill_color = st.color_picker("QR Color", "#000000")
    back_color = st.color_picker("Background Color", "#FFFFFF")

    box_size = st.slider("QR Size", 5, 15, 12)
    use_logo = st.checkbox("Add custom logo", value=False)

    if use_logo:
        logo_file = st.file_uploader("Upload Logo (optional)", type=["png", "jpg"])
        
        if logo_file is None:
                logo_file="logo.png"

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
        if fill_color == back_color:
            st.error("❌ QR color and background cannot be same")
            st.stop()
            
        img = qr.QRCode(
            version=None,
            box_size=box_size,
            border=3,
        )
        img.add_data(url)
        img.make(fit=True)

        img = img.make_image(fill_color=fill_color, back_color=back_color)
        # Add logo if uploaded
        if use_logo:
            if logo_file is not None:
                logo = Image.open(logo_file)
                # Resize logo
                qr_width, qr_height = img.size
                logo_size = qr_width // 7
                logo = logo.resize((logo_size, logo_size))

                # 👉 Create circular mask
                mask = Image.new("L", (logo_size, logo_size), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, logo_size, logo_size), fill=255)
                logo.putalpha(mask)
                # Position logo at center
                pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
                img.paste(logo, pos, mask=logo)

        buf = BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        st.image(buf.getvalue(),width=400)

        st.download_button(
            label="Download QR",
            data=buf.getvalue(),
            file_name=name if name.endswith('.png') else name + '.png',
            mime="image/png"
        )

    else:
        st.warning("Please enter some text")

