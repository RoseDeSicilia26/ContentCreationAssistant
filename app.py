import streamlit as st
import anthropic
import base64


def call_ai(content, writer, audiences, creativity_level=0):

    client = anthropic.Anthropic(
        api_key="key",
    )

    message = client.messages.create(
        model="claude-3-opus-20240229",
        temperature=creativity_level,
        system= f"From the perspective of {writer}, write an article for an audience of {audiences} based on the upcoming content.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"From the perspective of {writer}, write an article for an audience of {audiences} based on the following content: {content}"
                    }
                ]
            }
        ]
    )
    return message.content.text

def generate_content(content, writers=["David Ogilvy"], audiences=["IT Staff"], creativity_level=0):
    results = []

    for writer in writers:
        result = call_ai(content, writer, audiences, creativity_level)
        results.append(result)

    return results

import random

def generate_ipsum():

    size = random.randint(3, 7)

    ipsum_array = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."] * size
    
    return ipsum_array



def main():
    
    with st.sidebar:

        created_content = []
        uploaded_text = ""
        pasted_text = ""

        st.title("Content Creation Assistant")

        st.markdown("<h4>Upload your Content</h4>", unsafe_allow_html=True)
        
        # st.markdown("<br>", unsafe_allow_html=True)

        # File upload
        uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

        if uploaded_file is not None:
            uploaded_text = uploaded_file.getvalue().decode("utf-8")

            show_text = st.checkbox("Show Uploaded Text")

            if show_text:
                uploaded_text = "||" + st.text_area("Edit Uploaded Text", value=uploaded_text, height=200)

        st.markdown("<h4>OR</h4>", unsafe_allow_html=True)


        # File pasted
        pasted_text = "||" + st.text_area("Paste your content", height=200)

        


        st.markdown("<hr>", unsafe_allow_html=True)


        ## ------------------------------------------------------------------------ ##

        st.markdown("<h3>Create your content</h3>", unsafe_allow_html=True)

        writers = ["Gary C Halbert", "Joseph Sugarman", "David Ogilvy", "Other"]

        # Multiselect for selecting multiple writers
        selected_writers = st.multiselect("Select writers:", writers)

        if "Other" in selected_writers:
            new_writer = st.text_input("Enter new writer:")
            if new_writer:
                writers.append(new_writer)

        # # Display selected writers
        # st.write("Selected Writers:")
        # for w in selected_writers:
        #     st.write(w)
        # st.write(selected_writers)
       
        audience = ["IT Technician", "IT Technician", "IT Technician", "Other"]

        # Multiselect for selecting multiple writers
        selected_audience = st.multiselect("Select audience:", audience)

        if "Other" in selected_audience:
            new_audience = st.text_input("Enter new audience:")
            if new_audience:
                audience.append(new_audience)

        # # Display selected writers
        # st.write("Selected adueince:")
        # for a in selected_audience:
        #     st.write(a)
        # st.write(selected_audience)

        st.markdown("<hr>", unsafe_allow_html=True) 

        st.markdown("""
        <style>
        .st-emotion-cache-hc3laj {
            width: 100%;
        }
        </style> """, unsafe_allow_html=True)

        create_content_button = st.button("Create")

        if create_content_button:
            #st.write("please upload")
            if (uploaded_text == "||" or uploaded_text == "") and (pasted_text == "||" or pasted_text == ""):
                st.error("Please upload or paste content before creating.")
                
            else:
                if uploaded_text != "||" and uploaded_text != "":
                    content = uploaded_text

                    created_content = generate_ipsum()

                elif pasted_text != "||":
                    content = pasted_text

                    created_content = generate_ipsum()

        



    ## ------------------------------------------------------------------------ ##


    st.header("Content")


    # Displaying generated content with expanders
    if len(created_content) > 0:
        for idx, text in enumerate(created_content):
            expander_title = f"Content {idx + 1}"
            expander = st.expander(expander_title)
            # expander.write(text)
            updated_text = expander.text_area(f"Improve Content {idx + 1}", value=text, height=200)

            expander_download_button = expander.download_button(f"Download Content {idx + 1}", text)






    # CSS

    # st.markdown("""
    #     <style>
    #     .st-emotion-cache-hc3laj {
    #         width: 100%;
    #         color: green;
    #         background-color: transparent;
    #         border: 1px solid green;
    #         padding: 5px 10px;
    #         border-radius: 5px;
    #     }
    #     .st-emotion-cache-hc3laj:hover {
    #         background-color: green;
    #         color: white;
    #         border-color: green;
    #     }
    #     .st-emotion-cache-hc3laj:active {
    #         background-color: green;
    #         border-color: green;
    #         color:white;
    #     }
                

    #     .st-emotion-cache-19rxjzo {
    #     float: right;
    #     color: green;
    #     background-color: transparent;
    #     border: 1px solid green;
    #     padding: 5px 10px;
    #     border-radius: 5px;
    #     }
    #     .st-emotion-cache-19rxjzo:hover {
    #         background-color: green;
    #         color: white;
    #         border-color: green;
    #     }
    #     .st-emotion-cache-19rxjzo:active {
    #         background-color: green;
    #         border-color: green;
    #     }
    #     </style>
    # """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()