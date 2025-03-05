styles = """<style>    
    .stAppHeader, .stAppToolbarq, .footer {
        display: none !important;
        opacity: 0 !important;
    }

    .stAppViewContainer {
        background: url("https://static.vecteezy.com/system/resources/thumbnails/001/971/264/small_2x/beautiful-cherry-blossom-with-bokeh-lights-background-concept-free-vector.jpg");
        background-size: contain;
    }
    
    .stAppViewContainer::before {
        content: '';
        width: 100%;
        height: 100%;
        background-color: rgba(255, 105, 180, 0.5);
        position: absolute;
        top: 0;
        left: 0;
        z-index:0;
    }

    .stProgress .st-cs {
        background-color: green;
    }

    header.st-emotion-cache-1avcm0n {
        opacity: 70%;
    }
    
    .st-emotion-cache-0 {
        background-color: white;
        text-align: center;
        border-radius: 1rem;
        color: black;
    }

    .st-key-container {
        padding: 1rem 2rem;
    }

    .st-key-container div {
        text-align: left !important;
    }
    
    .st-key-footer {
        position: fixed; 
        bottom: 0;
        pointer-events: none;
        padding: 0.2rem 0;
    }


    .progress-bar {
        width: 100%;
        height: 0.5rem;
        border-radius: 0.5rem;
        position: relative;
        overflow: hidden;
        border: 1px solid #888;
        background-color: #ddd;
        box-shadow: 0 0 10px -10px rgba(255, 255, 255, 0.79) inset;
    }

    .progress-bar-value {
        height: 100%;
        transition: 0.5s all
    }

    .rating {
        margin: 0.5rem 0;
    } 
</style>"""


def progress_bar(status: int):

    rating = ''
    if status == 6:
        rating = "✅ Strong Password!"
    elif status == 4:
        rating = "⚠️ Moderate Password - Consider adding more security features."
    else:
        rating = "❌ Weak Password - Improve it using the suggestions below."

    return f"""
        <div class="progress-bar">
          <div class="progress-bar-value" style="width: {round(status * 16.6)}%;
            background-color: {'green' if status == 6 else 'orange' if status >= 4 else 'red'};
          "></div>
        </div>
        
        <div class="rating">{rating}</div>
    """
