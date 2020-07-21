import plotly.express as px
import sys


def main(f_loc: str):
    x,  y = [], []
    with open(f_loc, 'r') as f:
        for line in f.readlines():
            dat = line.split()
            x.append(dat[0])
            y.append(dat[1])
    fig = px.scatter(x=x, y=y)
    fig.show()


if __name__ == '__main__':
    f_loc = sys.argv[1] if len(sys.argv) > 1 else 'V3.spec.out'
    main(f_loc)
