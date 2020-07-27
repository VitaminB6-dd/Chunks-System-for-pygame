
def load_map(path, chunk_size, tile_size):
    """

    :param path: the path of the file that contains the game map
    :param chunk_size: number of tiles in a chunk
    :param tile_size:the size of the tile in pixels
    :return: a dict with the chunk top left pos as the key and the rows and tiles as the value
    """
    map_file = open(path, "r")
    map_file_data = map_file.read()
    map_file.close()
    map_file_data = map_file_data.split("\n")
    un_chunked_game_map = []
    for row in map_file_data:
        un_chunked_game_map.append(list(row))
    game_map = {}
    chunk_list = []
    row_range = 0
    x = 0
    y = 0
    for number_of_chunks_vertically in range(len(un_chunked_game_map) // chunk_size):
        tile_range = 0
        for number_of_chunks_horizontally in range(math.ceil(len(un_chunked_game_map[0]) / chunk_size)):
            for row in un_chunked_game_map[row_range : row_range + chunk_size]:
                row_list = []
                for tile in row[tile_range : tile_range + chunk_size]:
                    if len(row_list) < chunk_size:
                        row_list.append(tile)

                if len(chunk_list) < chunk_size:
                    chunk_list.append(row_list)
            game_map.update({(x * chunk_size * tile_size, y * chunk_size * tile_size) : chunk_list})
            chunk_list = []
            x += 1
            tile_range += chunk_size
        row_range += chunk_size
        y += 1
        x = 0
    return game_map



# inside game loop------------------:
    tile_rects = []
    for chunks_pos in game_map:
        # iterating ove all the chunks
        # if chunk is in the screen draw it
        if abs(player_rect.center[X] - chunks_pos[X]) <= window_width + CHUNK_SIZE and \
                abs(player_rect.center[Y] - chunks_pos[Y]) <= window_height and \
                player_rect.center[X] - chunks_pos[X] >= -CHUNK_SIZE * tile_size - tile_size and \
                player_rect.center[Y] - chunks_pos[Y] >= -CHUNK_SIZE * tile_size - tile_size:

            chunks_in_range.append(chunks_pos)
            x = 0
            y = 0
            # iterating over rows and tile in the chunk
            for row in game_map[chunks_pos]:
                for tile in row:
                    # drawing things according to the tile type
                    if tile == "0":
                        pass
                        # pygame.draw.rect(screen, (255, 40, 40),cam.apply((chunks_pos[X] + (x * tile_size), chunks_pos[Y] + (y * tile_size), tile_size, tile_size)))

                    if tile == "1":
                        # pygame.draw.rect(screen, (40, 40, 40), ((chunks_pos[X] + x) * tile_size, (chunks_pos[Y] + y) * tile_size, tile_size, tile_size))
                        pygame.draw.rect(screen, (40, 40, 40), cam.apply((chunks_pos[X] + (x * tile_size), chunks_pos[Y] + (y * tile_size), tile_size, tile_size)))

                    if tile == "2":
                        # pygame.draw.rect(screen, (40, 40, 40), ((chunks_pos[X] + x) * tile_size, (chunks_pos[Y] + y) * tile_size, tile_size, tile_size))
                        pygame.draw.rect(screen, (255, 40, 40), cam.apply((chunks_pos[X] + (x * tile_size), chunks_pos[Y] + (y * tile_size), tile_size, tile_size)))

                    if tile != "0":
                        tile_rects.append(pygame.Rect((chunks_pos[X] + (x * tile_size), chunks_pos[Y] + (y * tile_size), tile_size, tile_size)))
                    x += 1
                y += 1
                x = 0