import streamlit as st
import random

def verify_user_input():
    None

def generate_content(): 
    st.session_state.clicked = True

    size = random.randint(3, 7)

    content = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."] * size

    st.session_state["content"] = content

def main():

    with st.sidebar:

        data_expander = st.expander("Upload data")

        with data_expander:
            ### File upload
            uploaded_file = data_expander.file_uploader("Upload a text file", type=["txt"])

            if uploaded_file is not None:
                uploaded_text = uploaded_file.getvalue().decode("utf-8")

                show_text = data_expander.checkbox("Show Uploaded Text")

                if show_text:
                    uploaded_text = data_expander.text_area("Edit Uploaded Text", value=uploaded_text, height=200)

            data_expander.markdown("<h4>OR</h4>", unsafe_allow_html=True)


            ### File pasted
            pasted_text = data_expander.text_area("Paste your content", height=120)


            ### WRITERS
            # Initialize session state if not already initialized
            if "writers" not in st.session_state:
                st.session_state["writers"] = ["Add", "Hello"]
            if "selected_writers" not in st.session_state:
                st.session_state["selected_writers"] = []

            # Multiselect for selecting writers
            st.session_state.selected_writers = data_expander.multiselect(
                "Select writers:",
                st.session_state.writers,
                default=[],  # Set default to an empty list to avoid NoneType error
                placeholder="Choose an option"
            )

            # If "Add" is selected, allow the user to enter a new writer
            if "Add" in st.session_state.selected_writers:
                new_writer = data_expander.text_input("Enter new writer:")
                if new_writer:
                    st.session_state.writers.append(new_writer)
                    st.session_state.selected_writers.append(new_writer)

            # data_expander.write(st.session_state["writers"])
            # data_expander.write(st.session_state["selected_writers"])


            ### TONE
            # Initialize session state if not already initialized
            if "tone" not in st.session_state:
                st.session_state["tone"] = ["professional", "Add"]
            if "selected_tone" not in st.session_state:
                st.session_state["selected_tone"] = []

            # Multiselect for selecting writers
            st.session_state.selected_tone = data_expander.multiselect(
                "Select tone:",
                st.session_state.tone,
                default=[],  # Set default to an empty list to avoid NoneType error
                placeholder="Choose an option"
            )

            # If "Add" is selected, allow the user to enter a new writer
            if "Add" in st.session_state.selected_tone:
                new_tone = data_expander.text_input("Enter new tone:")
                if new_tone:
                    st.session_state.tone.append(new_tone)
                    st.session_state.selected_tone.append(new_tone)

            # data_expander.write(st.session_state["tone"])
            # data_expander.write(st.session_state["selected_tone"])


        ### STEPS
        steps_expander = st.expander("Set up processing steps")

        with steps_expander:

            # add the key choices_len to the session_state
            if "n_steps" not in st.session_state:
                st.session_state["n_steps"] = 1

            if "instruction_options" not in st.session_state:
                st.session_state["instruction_options"] = ["Step 1", "Step 2", "Step 3"]

            if "sorted_selected_instructions" not in st.session_state:
                st.session_state["sorted_selected_instructions"] = [None] * 20
            

            instructions = st.container()
            buttons = st.container()

            with buttons:
                add, submit, remove = st.columns((1, 1, 1))
                with add:
                    if st.button("➕"):
                        st.session_state["n_steps"] += 1

                with submit:
                    st.button("submit")

                with remove:
                    if st.button("➖︎") and st.session_state["n_steps"] > 1:
                        st.session_state["n_steps"] -= 1
                        st.session_state.pop(f'{st.session_state["n_steps"]}')

            for x in range(st.session_state.n_steps):
                value = instructions.multiselect(f"Step {x+1}", st.session_state.instruction_options, placeholder="Select an instruction", key=f"{x+1}")
                if value is not None:
                    st.session_state.sorted_selected_instructions[x] = value

            # Create a form for adding a custom instruction
            with steps_expander.form("add_instruction_form"):
                new_instruction = st.text_area("Add a custom instruction")
                submit_button = st.form_submit_button("Add")
            
                if submit_button:
                    if new_instruction:
                        # st.session_state["instruction_options"] += [new_instruction]
                        st.session_state.instruction_options.append(new_instruction)
                        st.rerun()

            # st.write(st.session_state.sorted_selected_instructions)
            # st.write(st.session_state.instruction_options)


        ### GENERATE
        if "clicked" not in st.session_state:
            st.session_state.clicked = False

        st.button("Generate content", on_click=generate_content)





    if "content" not in st.session_state:
        st.session_state["content"] = []


    content_array = st.session_state.content
    for idx, content in enumerate(content_array):
        expander = st.expander(f"Content {idx + 1}")
        expander.write(content)
        update_text = expander.text_area(f"Improve Content {idx + 1}", value=content, height=200)



if __name__ == "__main__":
    main()
