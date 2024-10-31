WIDTH : int = 400
HEIGHT : int = 675

ENTRY_WIDTH : int = int(WIDTH / 10) - 2
COMBOBOX_WIDTH : int = ENTRY_WIDTH - 2

BG_COLOR : str = "#191919"
FG_COLOR : str = "#FFFFFF"
HL_COLOR : str = "#017300"
BLACK : str = "#000000"
GREY : str = "#808080"
HL_BG_COLOR : str = "#0000C5"

FONT = lambda size: ("Arial", size)
ENTRY_FONT_SIZE : int = 12
LABEL_FONT_SIZE : int = 14

ENTRY_PADY: int = 5
ENTRY_PADX: int = 10
ENTRY_IPADY : int = 3
LABEL_PADY: int = 10

SELECTION_STRATEGY = ["Selection strategy: BEST", "Selection strategy: ROULETTE", "Selection strategy: TOURNAMENT"]
CROSS_STRATEGY = ["Cross strategy: ONE POINT", "Selection strategy: TWO POINT"]
MUTATION_STRATEGY = ["Mutation strategy: ONE POINT", "Mutation strategy: TWO POINT", "Mutation strategy: BOUNDARY"]