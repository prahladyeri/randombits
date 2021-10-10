import uuid

readme = """```bash

This is an auto-generated github repository that just 
pushes some random bits to keep your github activity going.
Useful when you're on a vacation or just temporarily 
lost inspiration to code.

%code1%
%code2%
%code3%

Running:

python build.py
git add .
git commit -m "build: random bits"
git push
```
"""
def main():
    rm = readme
    rm = rm.replace('%code1%', str(uuid.uuid4()))
    rm = rm.replace('%code2%', str(uuid.uuid4()))
    rm = rm.replace('%code3%', str(uuid.uuid4()))
    open('readme.md', 'w').write(rm)
    
if __name__ == "__main__":
    main()