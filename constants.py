import ctypes

class constants(object):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 450
    POS_X = 700
    POS_Y = 450
    BACKGROUND_Y = 73

    #================ creature parameter changing
    FED_CHANGE = 3
    ENERGY_CHANGE_SLEEP = 2
    ENERGY_CHANGE_AWAKEN = 1
    LOVE_CHANGE = 2
    HEALTH_CHANGE = 2
    TOILET_MUST_CHANGE = 2

    #================ creature movement board
    MOV_X_0 = 25
    MOV_Y_0 = 150
    MOV_WIDTH = WINDOW_WIDTH - MOV_X_0*2
    SIN_PROPORTION = 20
    # MOV_Y_0 = 110
    # MOV_HEIGHT = 190

    #================ images
    BACKGR_LIGHT = 0
    HEART1 = 1
    HEART2 = 2

    NEWB_RIGHT = 3
    NEWB_LEFT = 4
    NEWB_CENTR = 5

    GOOD_STYLE = """
    QProgressBar {
    text-align: top;
    padding: 1px;
    border-radius: 7px;
    height: 3px;
    }

    QProgressBar::chunk {
    background: #429000;
    border-radius: 7px;
    }
    """

    WARNING_STYLE = """
    QProgressBar {
    border: 0px;
    text-align: top;
    padding: 1px;
    border-radius: 7px;
    height: 3px;
    }

    QProgressBar::chunk {
    background: #c3ce08;
    border-radius: 7px;
    }
    """

    ALARM_STYLE = """
    QProgressBar {
    text-align: top;
    padding: 1px;
    border-radius: 7px;
    height: 3px;
    }

    QProgressBar::chunk {
    background: #b61a0b;
    border-radius: 7px;
    }
    """
