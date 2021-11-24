import os, sys
from path import Path

# 폴더 생성
def main():
    for path in Path:
        p = path.value
        try:
            if not os.path.exists(p):
                os.makedirs(p)
        except OSError:
            print("Error : Can not initialize path :" + p)

if __name__ == "__main__":
    main(sys.argv)
