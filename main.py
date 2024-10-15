import pygame
from maze import SearchSpace
from algos import DFS, BFS, Dijkstra, A_star
from const import RES, GREY, RED, BLUE
import argparse

def main(algo:str):
    your_name = 'your name goes here'
    pygame.init()
    pygame.display.set_caption(f'{your_name} - {algo}')
    sc = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(GREY))

    g = SearchSpace()
    g.draw(sc)
    clock.tick(200)

    if algo == 'DFS':
        DFS(g, sc)
    elif algo == 'BFS':
        BFS(g, sc)
    elif algo == 'Dijkstra':
        Dijkstra(g, sc)
    elif algo == 'A_star':
        A_star(g, sc)
    else:
        raise NotImplementedError('Not implemented')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__=='__main__':  
     parser = argparse.ArgumentParser(description='Search algorithms')
     parser.add_argument('--algo', type=str, help='Enter search algorithm', default=input("Nhap thuat toan muon chay: "))

     args = parser.parse_args()
     main(args.algo)
