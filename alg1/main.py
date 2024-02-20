class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class Cube:
    # Initialize Cube as an object - instance of "Cube" class.
    def __init__(self, init_state) -> None:
        self.init_state = init_state

        self.STAGES = {
            0: {"main": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "sides": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "back": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]]},
            1: {"main": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "sides": [[1, 1, 1],[1, 1, 1],[2 ,1 ,2]], "back": [[2, 1, 2],[1, 1, 1],[2 ,1 ,2]]},
            2: {"main": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "sides": [[1, 1, 1],[1, 1, 1],[0 ,1 ,0]], "back": [[0, 1, 0],[1, 1, 1],[0 ,1 ,0]]},
            3: {"main": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "sides": [[1, 1, 1],[1, 1, 1],[0 ,0 ,0]], "back": [[0, 1, 0],[1, 1, 1],[0 ,1 ,0]]},
            4: {"main": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "sides": [[1, 1, 1],[1, 1, 1],[0 ,0 ,0]], "back": [[0, 0, 0],[0, 1, 0],[0 ,0 ,0]]},
            5: {"main": [[1, 1, 1],[1, 1, 1],[1 ,1 ,1]], "sides": [[1, 1, 1],[0, 1, 0],[0 ,0 ,0]], "back": [[0, 0, 0],[0, 1, 0],[0 ,0 ,0]]},
            6: {"main": [[0, 1, 0],[1, 1, 1],[0 ,1 ,0]], "sides": [[0, 1, 0],[0, 1, 0],[0 ,0 ,0]], "back": [[0, 0, 0],[0, 1, 0],[0 ,0 ,0]]},
            7: {"main": [[0, 0, 0],[0, 1, 0],[0 ,0 ,0]], "sides": [[0, 0, 0],[0, 1, 0],[0 ,0 ,0]], "back": [[0, 0, 0],[0, 1, 0],[0 ,0 ,0]]},
        }
        self.sides = ["W", "B", "Y", "G", "O", "R"]
        self.goal_state = {
            "W": {"array": [["W", "W", "W"],["W", "W", "W"],["W", "W", "W"]]},
            "B": {"array": [["B", "B", "B"],["B", "B", "B"],["B", "B", "B"]]},
            "Y": {"array": [["Y", "Y", "Y"],["Y", "Y", "Y"],["Y", "Y", "Y"]]},
            "G": {"array": [["G", "G", "G"],["G", "G", "G"],["G", "G", "G"]]},
            "O": {"array": [["O", "O", "O"],["O", "O", "O"],["O", "O", "O"]]},
            "R": {"array": [["R", "R", "R"],["R", "R", "R"],["R", "R", "R"]]},
        }

        self.main_side = self._find_main()
        self.current_stage = self._stage_finder(init_state)

        self.performing_side = self.main_side
    
    # Find Main Face => most completed face
    def _find_main(self):
        _sides = {"W": 0, "B": 0, "Y": 0, "G": 0, "O": 0, "R": 0}
        for _side in self.sides:
            for _line in self.init_state[_side]["F"]:
                for _block in _line:
                    if _block == _side:
                        _sides[_side] += 1

        _max = ""
        _c = 0
        for __side in self.sides:
            if _sides[__side] > _c:
                _max = __side
                _c = _sides[__side]
        return _max
    
    # Find current cube stage in algorithm
    def _stage_finder(self, current_state):
        _main_face_name = self.main_side
        print(_main_face_name)
        _side_face_names = [current_state[_main_face_name]["U"], current_state[_main_face_name]["R"], current_state[_main_face_name]["D"], current_state[_main_face_name]["L"]]
        _back_face_name = current_state[_main_face_name]["B"]

        _correct = False
        _stage = 0
        while _stage < 8 and _correct == False:
            _check = True
            print("stage_"+str(_stage))
            _main_face_test = self.STAGES[_stage]["main"]
            _side_face_test = self.STAGES[_stage]["sides"]
            _back_face_test = self.STAGES[_stage]["sides"]
            # Main face check
            print("main")
            for i in range(3):
                for j in range(3):
                    if _main_face_test[i][j] == 1:
                        if current_state[_main_face_name]["F"][i][j] != _main_face_name:
                            _check = False
                            print("false_m1")
                    elif _main_face_test[i][j] == 0:
                        if current_state[_main_face_name]["F"][i][j] == _main_face_name:
                            _check = False
                            print("false_m0")

            # Side faces check
            print("side")
            for _side_name in _side_face_names:
                # print("side_"+_side_name)
                for i in range(3):
                    for j in range(3):
                        if _side_face_test[i][j] == 1:
                            if current_state[_side_name]["F"][i][j] != _side_name:
                                _check = False
                                print("false_s1")
                        elif _side_face_test[i][j] == 0:
                            if current_state[_side_name]["F"][i][j] == _side_name:
                                _check = False
                                print("false_s0")
            # Back face check
            print("back")
            for i in range(3):
                for j in range(3):
                    if _back_face_test[i][j] == 1:
                        if current_state[_back_face_name]["F"][i][j] != _back_face_name:
                            _check = False
                            print("false_b1")
                    elif _back_face_test[i][j] == 0:
                        if current_state[_back_face_name]["F"][i][j] == _back_face_name:
                            _check = False
                            print("false_b0")
            
            print("end_"+str(_stage))
            _correct = _check
            _stage += 1
            
        # Return Stage
        print("end")
        print(_stage)
        return _stage

    # Test whether current-state is the goal-state
    def GoalTest(self, node):
        return self.goal_state == node.state

