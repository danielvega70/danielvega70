def draw_walls(self):
    wallcolor = Color(140, 140, 140)

    for wall in self.walls:
        nrow, ncol = wall

        pos_x = self.field_rect.left + ncol * self.GRID_SIZE + self.GRID_SIZE / 2
        pos_y = self.field_rect.top + nrow * self.GRID_SIZE + self.GRID_SIZE / 2
        radius = 3

        pygame.draw.polygon(self.screen, wallcolor,
            [   (pos_x - radius, pos_y), (pos_x, pos_y + radius),
                (pos_x + radius, pos_y), (pos_x, pos_y - radius)])

        if (nrow + 1, ncol) in self.walls:
            pygame.draw.line(self.screen, wallcolor,
                (pos_x, pos_y), (pos_x, pos_y + self.GRID_SIZE), 3)
        if (nrow, ncol + 1) in self.walls:
            pygame.draw.line(self.screen, wallcolor,
                (pos_x, pos_y), (pos_x + self.GRID_SIZE, pos_y), 3)
        else: # draw right wall of the field if there is no wall to the right of the current wall
            ncol_to_right = ncol + 1
            while (nrow, ncol_to_right) in self.walls:
                ncol_to_right += 1
            pos_x_right = self.field_rect.left + ncol_to_right * self.GRID_SIZE + self.GRID_SIZE / 2
            pygame.draw.line(self.screen, wallcolor,
                (pos_x + self.GRID_SIZE / 2, pos_y), (pos_x_right - self.GRID_SIZE / 2, pos_y), 3)
