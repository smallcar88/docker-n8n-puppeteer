from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/tex2pdf', methods=['POST'])
def convert_tex_to_pdf():
    tex_content = request.data.decode('utf-8')
    input_file = 'input.tex'
    with open(input_file, 'w') as file:
        file.write(tex_content)

@app.route('/md2docx', methods=['POST'])
def convert_markdown_to_word():
    markdown_content = request.data.decode('utf-8')
    input_file = 'input.md'
    output_file = 'output.docx'

    with open(input_file, 'w') as file:
        file.write(markdown_content)

    try:
        subprocess.run(['pandoc', input_file, '-o', output_file], check=True)
        return send_file(output_file, as_attachment=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500
    finally:
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
