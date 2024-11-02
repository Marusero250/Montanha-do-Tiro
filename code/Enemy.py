#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = ENTITY_SPEED[self.name]
        self.direction = 1  # 1 para baixo, -1 para cima

    def move(self):
        # Movimento horizontal
        self.rect.centerx -= ENTITY_SPEED[self.name]
        
        # Movimento vertical específico para o Enemy3
        if self.name == 'Enemy3':
            self.rect.centery += self.vertical_speed * self.direction
            
            # Verifica se atingiu a borda inferior
            if self.rect.bottom >= WIN_HEIGHT:
                self.direction = -1  # Muda a direção para cima
            
            # Verifica se atingiu a borda superior
            elif self.rect.top <= 0:
                self.direction = 1   # Muda a direção para baixo
                self.vertical_speed = ENTITY_SPEED[self.name] * 2  # Dobra a velocidade

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

