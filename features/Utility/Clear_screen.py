import streamlit.components.v1 as components
import streamlit as st

def Clear_screen():
    """
    Clears the visible content of the screen in a Streamlit app
    by dynamically calculating the number of blank lines (`st.write(" ")`)
    needed based on the device's screen resolution.
    """
    # JavaScript to determine screen height and orientation
    js_code = """
    <script>
    const getResolution = () => {
        let height = window.innerHeight; // Screen height in pixels
        let width = window.innerWidth; // Screen width in pixels
        let orientation = (width > height) ? "landscape" : "portrait";
        return `${height},${width},${orientation}`;
    };
    document.write(`<div id='resolution'>${getResolution()}</div>`);
    </script>
    """

    # Render the JavaScript in Streamlit and capture the screen resolution
    resolution_html = components.html(js_code, height=0, width=0)
    
    # Extract resolution data
    try:
        resolution_data = resolution_html.split(",")
        screen_height = int(resolution_data[0])
        orientation = resolution_data[2]
    except:
        # Default to a safe value if JavaScript fails
        screen_height = 800
        orientation = "portrait"

    # Approximate height of a single st.write(" ") line in pixels
    line_height = 20  # Adjust based on visual testing on your devices

    # Calculate the number of lines required to clear the screen
    num_lines = screen_height // line_height

    # Write blank lines to clear the screen
    for _ in range(num_lines):
        st.write(" ")

    # Optionally return the calculation details for debugging
    return {
        "screen_height": screen_height,
        "line_height": line_height,
        "num_lines": num_lines,
        "orientation": orientation
    }
