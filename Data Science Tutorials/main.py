from pyscript import document, window
import io
import sys


window.fadeOutOverlay()


def update_max_height(element):

    element.style.transition = ''

    contentHeight = f'{element.scrollHeight + 10}px'
    print(contentHeight)
    element.style.transition = 'max-height 0.5s linear, opacity 1s ease-in'
    element.style.maxHeight = contentHeight
    element.style.opacity = 1
    # element.style.transition = current_transition

def run_python_code(*args):

    print('Executing Python Code!')

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    code = window.editor.getValue()
    exec(code)

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    html_output = document.getElementById("output")
    html_output.innerHTML = output
    update_max_height(html_output)
