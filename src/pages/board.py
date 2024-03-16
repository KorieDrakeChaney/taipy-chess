from taipy.gui import Markdown
import pandas as pd

data = pd.DataFrame({
        "Moves": [
            [4648, 7385, 9355, 14092, 14740, 9605, 33166, 5591], 
            [5181, 9271, 11201, 21750, 21259, 11041, 10223, 6456], 
            [12877, 15702, 36837, 24877, 23471, 43422, 17203, 14682], 
            [13890, 21438, 30769, 48608, 44095, 25063, 24110, 14834], 
            [14044, 23664, 28632, 46990, 46824, 23813, 26006, 15273], 
            [41535, 15498, 38283, 27047, 27660, 42652, 18779, 15933], 
            [5221, 10305, 11607, 23388, 24844, 12535, 12867, 6571], 
            [4857, 7322, 9908, 14454, 13997, 10247, 6421, 5855]
            ],
    "Files": ["1", "2", "3", "4", "5", "6", "7", "8"],
    "Ranks": ["a", "b", "c", "d", "e", "f", "g", "h"]
})

layout = {
    "title": "Heatmap of Chessboard",
    "xaxis": {
        "title": "Ranks",
    },
    "yaxis": {
        "title": "Files",
    },
    "plot_config" : {
        "editable" : False,
        "scrollZoom": False,
        "displayModeBar": False,
    },
}


board = Markdown("src/pages/board.md")