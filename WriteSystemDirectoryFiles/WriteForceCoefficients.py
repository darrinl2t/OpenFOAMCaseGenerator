class WriteForceCoefficients:
    def __init__(self, file_manager, flow_properties):
        self.file_manager = file_manager
        self.flow_properties = flow_properties

    def write_force_coefficients(self):
        lift_dir = ('(' + str(self.flow_properties['lift_direction'][0]) + ' ' +
                    str(self.flow_properties['lift_direction'][1]) + ' ' +
                    str(self.flow_properties['lift_direction'][2]) + ')')
        drag_dir = ('(' + str(self.flow_properties['drag_direction'][0]) + ' ' +
                    str(self.flow_properties['drag_direction'][1]) + ' ' +
                    str(self.flow_properties['drag_direction'][2]) + ')')
        pitch_dir = ('(' + str(self.flow_properties['pitch_axis_direction'][0]) + ' ' +
                     str(self.flow_properties['pitch_axis_direction'][1]) + ' ' +
                     str(self.flow_properties['pitch_axis_direction'][2]) + ')')
        cofr = ('(' + str(self.flow_properties['center_of_roation'][0]) + ' ' +
                str(self.flow_properties['center_of_roation'][1]) + ' ' +
                str(self.flow_properties['center_of_roation'][2]) + ')')

        file_id = self.file_manager.create_file('system', 'forceCoefficients')
        self.file_manager.write(file_id,
                                '/*--------------------------------*- C++ -*----------------------------------*\\\n')
        self.file_manager.write(file_id,
                                '| =========                 |                                                 |\n')
        self.file_manager.write(file_id,
                                '| \\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
        self.file_manager.write(file_id,
                                '|  \\\    /   O peration     | Version:  ' + self.file_manager.get_version() +
                                '                                 |\n')
        self.file_manager.write(file_id,
                                '|   \\\  /    A nd           | Web:      www.OpenFOAM.com                      |\n')
        self.file_manager.write(file_id,
                                '|    \\\/     M anipulation  |                                                 |\n')
        self.file_manager.write(file_id,
                                '\*---------------------------------------------------------------------------*/\n')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id, 'forceCoeffs1\n')
        self.file_manager.write(file_id, '{\n')
        self.file_manager.write(file_id, '    type            forceCoeffs;\n')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id, '    libs            (forces);\n')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id, '    writeControl    timeStep;\n')
        self.file_manager.write(file_id, '    timeInterval    1;\n')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id, '    log             yes;\n')
        self.file_manager.write(file_id, '\n')
        if len(self.flow_properties['wall_boundaries']) == 1:
            self.file_manager.write(file_id, '    patches         (' + self.flow_properties['wall_boundaries'][0] +
                                    ');\n')
        else:
            self.file_manager.write(file_id, '    patches         (')
            temp_str = ''
            for boundary in self.flow_properties['wall_boundaries']:
                temp_str += boundary + ' '
            self.file_manager.write(file_id, temp_str[:-1] + ');\n')
        self.file_manager.write(file_id, '    rho             rhoInf;\n')
        self.file_manager.write(file_id, '    rhoInf          1;\n')
        self.file_manager.write(file_id, '    liftDir         ' + lift_dir + ';\n')
        self.file_manager.write(file_id, '    dragDir         ' + drag_dir + ';\n')
        self.file_manager.write(file_id, '    CofR            ' + cofr + ';\n')
        self.file_manager.write(file_id, '    pitchAxis       ' + pitch_dir + ';\n')
        self.file_manager.write(file_id,
                                '    magUInf         ' + str(self.flow_properties['velocity_magnitude']) + ';\n')
        self.file_manager.write(file_id, '    lRef            ' + str(self.flow_properties['reference_length']) + ';\n')
        self.file_manager.write(file_id, '    Aref            ' + str(self.flow_properties['reference_area']) + ';\n')
        self.file_manager.write(file_id, '}\n')
        self.file_manager.write(file_id, '\n')
        self.file_manager.write(file_id,
                                '// ************************************************************************* //\n')