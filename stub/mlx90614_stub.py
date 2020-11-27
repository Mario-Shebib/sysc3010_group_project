
import sys
class no_MLX90614:

    def __init__(self):
        try:
            with open("ambient_temperature.txt", "r") as ambient_temp_file:
                self.ambient_temp = ambient_temp_file.read().strip()
            with open("ir_temperature.txt", "r") as ir_temp_file:
                self.ir_temp = ir_temp_file.read().strip()
        except FileNotFoundError as e:
            print("Could not open testcase files.")
            exit(1)
    
    def get_ambient_temp(self):
        self.ambient_temp
        return self.ambient_temp
    def get_ir_temp(self):
        return self.ir_temp
        
