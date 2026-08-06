# Space Threads Impact

## Project Overview

The goal of this project was to develop a multithreaded game demonstrating the use of **threads**, **mutexes**, and **semaphores** for synchronization in Python.

The game is inspired by the classic **Space Impact** available on the Nokia 3310.

## From `curses` to `pygame`

The initial version of the game was implemented using the **curses** library, allowing it to be fully playable in the terminal.

As the project evolved, we planned to introduce more advanced gameplay mechanics and graphical features that were difficult or impossible to implement with `curses`. For this reason, the project was rewritten using the **pygame** library, providing greater flexibility and a richer graphical interface.

## User Interface

The game features a graphical user interface built with **pygame**, including animated sprites, player and enemy ships, projectiles, collectible power-ups, score tracking, and a scrolling background to create a classic arcade shooter experience.

## Multithreading and Synchronization

The game relies on multiple threads and synchronization primitives to coordinate gameplay while preventing race conditions.

### Synchronization Primitives

* **`threading.Semaphore(CONFIG.BOOSTS_LIMIT)`**

  * Limits the maximum number of power-ups that can exist simultaneously.

* **`threading.Semaphore(CONFIG.MAX_ENEMY_NUMBER)`**

  * Restricts the number of enemies that may appear at the same time.

* **`Game.background_lock = threading.Semaphore(1)`**

  * Ensures synchronized access when updating scrolling background elements.

* **`Game.points_lock = threading.Lock()`**

  * Protects the shared score variable from concurrent modifications.

* **`Player.ammo_limit_lock = threading.Semaphore(self.ammo_capacity)`**

  * Controls the player's ammunition capacity by preventing shooting until ammunition has been reloaded.

### Threads

* **Enemy Spawner Thread**

  ```python
  enemy_spawner = threading.Thread(target=spawn_enemy, args=(game, game_over_event))
  ```

  Continuously spawns new enemies while respecting the configured enemy limit.

* **Game Timer Thread**

  ```python
  timer_thread = threading.Thread(target=timer, args=(game, game_over_event))
  ```

  Tracks the elapsed game time independently of the main game loop.

These synchronization mechanisms ensure that multiple game systems can operate concurrently while maintaining consistent shared state and preventing race conditions.



# Space Threads Impact
## Opis projektu
Założeniem projektu było wykorzystanie stworzenie aplikacji wykorzystującej wielowątkowość oraz sekcje krytyczne (mutexy i semaphory).
Aplikacja jest grą, która jest inspirowana starą grą [Space Impact](https://www.youtube.com/watch?v=tKobl50jrLk)  na Nokie 3310.

## Z curses do pygame
Wstępna wersja gry wykorzystywała bibliotekę curses aby gra była w pełni grywalna z poziomu terminalu. 
![Cursed Space Impact](https://github.com/sergiuszdev/SO2-space-threads-invader/blob/main/cursed-game-image)
Funkcjonalności, które planowaliśmy zaimplementować, nie były możliwe do zrealizowania przy użyciu curses i zaczęliśmy przepisywać grę przy użyciu biblioteki pygame.

## UI 
![UI](https://github.com/sergiuszdev/SO2-space-threads-invader/blob/main/ui.png?raw=true)
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
