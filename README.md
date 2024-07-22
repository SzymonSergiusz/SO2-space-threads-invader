# Space Threads Impact
## Opis projektu
Założeniem projektu było wykorzystanie stworzenie aplikacji wykorzystującej wielowątkowość oraz sekcje krytyczne (mutexy i semaphory).
Aplikacja jest grą, która jest inspirowana starą grą [Space Impact](https://www.youtube.com/watch?v=tKobl50jrLk)  na Nokie 3310.

## Z curses do pygame
Wstępna wersja gry wykorzystywała bibliotekę curses aby gra była w pełni grywalna z poziomu terminalu. 
![Cursed Space Impact](https://github.com/SzymonSergiusz/SO2-space-threads-invader/blob/main/cursed-game-image)
Funkcjonalności, które planowaliśmy zaimplementować, nie były możliwe do zrealizowania przy użyciu curses i zaczęliśmy przepisywać grę przy użyciu biblioteki pygame.

## UI 
![UI](https://github.com/SzymonSergiusz/SO2-space-threads-invader/blob/main/ui.png?raw=true)
## Wątki
- threading.Semaphore(CONFIG.BOOSTS_LIMIT)
Semaphor odpowiedzialny za ustawienie limitu pojawiąjących się ulepszeń w grze w danym momencie
- threading.Semaphore(CONFIG.MAX_ENEMY_NUMBER) 
Semaphor odpowiedzialny za ograniczenie pojawiających się przeciwników
-  Game.background_lock = threading.Semaphore(1)
Semaphor odpowiedzialny za ograniczenie się elementów przelatujących w tle
-  Game.points_lock = threading.Lock() 
Mutex odpowiedzialny za blokowanie dostępu do zmiennej odpowiedzialnej za liczenie punktów zdobytych przez gracza
- enemy_spawner = threading.Thread(target=spawn_enemy, args=(game,game_over_event))
Wątek odpowiedzialny generowanie nowych przeciwników
- timer_thread = threading.Thread(target=timer, args=(game,game_over_event))
Wątek odpowiedzialny za liczenie czasu rozgrywki
- Player.ammo_limit_lock = threading.Semaphore(self.ammo_capacity)
Semaphor odpowiedzialny za blokowanie możliwości strzelania przez gracza aż do czasu przeładowania.
