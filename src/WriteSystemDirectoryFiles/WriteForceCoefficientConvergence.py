from src import GlobalVariables as Parameters


class WriteForceCoefficientConvergence:
    def __init__(self, properties, file_manager):
        self.properties = properties
        self.file_manager = file_manager

    def write_triggers(self):
        wait_n_time_steps =\
            str(self.properties['convergence_control']['time_steps_to_wait_before_checking_convergence'])
        file_id = self.file_manager.create_file('system/include', 'forceCoefficientTrigger')
        self.file_manager.write_header(file_id, 'dictionary', 'system', 'forceCoefficientConvergenceTrigger')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id, 'runTimeControl1\n')
        self.file_manager.write(file_id, '{\n')
        self.file_manager.write(file_id, '    type            runTimeControl;\n')
        self.file_manager.write(file_id, '    libs            (utilityFunctionObjects);\n')
        self.file_manager.write(file_id, '    controlMode     trigger;\n')
        self.file_manager.write(file_id, '    triggerStart    1;\n')
        self.file_manager.write(file_id, '    conditions\n')
        self.file_manager.write(file_id, '    {\n')
        if self.properties['convergence_control']['integral_convergence_criterion'] == Parameters.C_D:
            self.__write_trigger(file_id, 'Cd')
        elif self.properties['convergence_control']['integral_convergence_criterion'] == Parameters.C_L:
            self.__write_trigger(file_id, 'Cl')
        elif self.properties['convergence_control']['integral_convergence_criterion'] == Parameters.C_S:
            self.__write_trigger(file_id, 'Cs')
        elif self.properties['convergence_control']['integral_convergence_criterion'] == Parameters.C_M_YAW:
            self.__write_trigger(file_id, 'CmYaw')
        elif self.properties['convergence_control']['integral_convergence_criterion'] == Parameters.C_M_ROLL:
            self.__write_trigger(file_id, 'CmRoll')
        elif self.properties['convergence_control']['integral_convergence_criterion'] == Parameters.C_M_PITCH:
            self.__write_trigger(file_id, 'CmPitch')
        self.file_manager.write(file_id, '    }\n')
        self.file_manager.write(file_id, '}\n')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id, 'runTimeControl2\n')
        self.file_manager.write(file_id, '{\n')
        self.file_manager.write(file_id, '    type            runTimeControl;\n')
        self.file_manager.write(file_id, '    libs            (utilityFunctionObjects);\n')
        self.file_manager.write(file_id, '    conditions\n')
        self.file_manager.write(file_id, '    {\n')
        self.file_manager.write(file_id, '        conditions1\n')
        self.file_manager.write(file_id, '        {\n')
        self.file_manager.write(file_id, '            type            maxDuration;\n')
        self.file_manager.write(file_id, '            duration        ' + wait_n_time_steps + ';\n')
        self.file_manager.write(file_id, '        }\n')
        self.file_manager.write(file_id, '    }\n')
        self.file_manager.write(file_id, '    satisfiedAction setTrigger;\n')
        self.file_manager.write(file_id, '    trigger         1;\n')
        self.file_manager.write(file_id, '}\n')
        self.file_manager.write(file_id,
                                '// ************************************************************************* //\n')

    def __write_trigger(self, file_id, quantity_to_write):
        convergence = str(self.properties['convergence_control']['integral_quantities_convergence_threshold'])
        averaging_time = str(self.properties['convergence_control']['averaging_time_steps'])

        self.file_manager.write(file_id, '        condition1\n')
        self.file_manager.write(file_id, '        {\n')
        self.file_manager.write(file_id, '            type            average;\n')
        self.file_manager.write(file_id, '            functionObject  forceCoeffs;\n')
        self.file_manager.write(file_id, '            fields          (' + quantity_to_write + ');\n')
        self.file_manager.write(file_id, '            tolerance       ' + convergence + ';\n')
        self.file_manager.write(file_id, '            window          ' + averaging_time + ';\n')
        self.file_manager.write(file_id, '            windowType      approximate;\n')
        self.file_manager.write(file_id, '        }\n')

