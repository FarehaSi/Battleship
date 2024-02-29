# Combat of Battleship
<a href="https://battleship-p3-433febf8714b.herokuapp.com/" target="_blank">Combat of Battleship</a>, popularly known worldwide as just ‘Battleship’, is usually a pencil and paper game that dates back to World War I. It is a guessing game for two players that is played on ruled grids where players take turns calling shots at the other player’s ships that are concealed. The objective of the game is to destroy the opponent’s fleet.
<br>
Combat of Battleship is a Python terminal game, meant for a single user to play against the computer. There are five battleships on each game board (5x5). The player is to guess the position of the Computer's battleships. Whoever hits all 5 of the opponents' battleships first, wins the game. The game can be used to kill time or simply have fun with! It is targeted at individuals of all age groups and regions!
![WebsiteMockup](https://user-images.githubusercontent.com/116716786/225623836-5e05fb86-4bf3-4605-97a6-0fcb109b897c.png)
## Features
![FirstLook](https://user-images.githubusercontent.com/116716786/225663186-aab9d1a8-1b12-46d6-a843-05a52d085242.png)

This is the first look, that the users experience as they run the game in the terminal.
- A welcome message greets the user, followed by brief instructions to help the player understand the concept of the game.
- Game boards are displayed and the user is asked to choose which spot on the Computer's board they wish to hit.

![FirstTurn](https://user-images.githubusercontent.com/116716786/225663240-8c9fc1a2-eb48-42ba-b39b-c849fde65700.png)

Once the player makes a selection, the following happens:
- The computer also chooses a spot to hit 
- Both the selections are printed to the console
- Updated boards are printed to the terminal. First one displays the user's targets and the other the computer's. 
- A reference table is simultaneously printed alongside to facilitate user selection.
- A "-" on the board represents a miss
- An "x" represents a hit
- Beneath the results from the first move, the user is prompted to take the next turn
- The game continues until either the player or the computer hits all 5 of the opponent's battleships.
### Features Left to Implement
The game can be expanded to allow the player:
- To input their own name to give a personal feel
- To select board size and number of ships
- To have ships larger than 1x1
## Testing
The game has been manually tested using the following methods:
- The game was run in both the GitPod Console and the Code Institute Heroku Terminal
- Invalid inputs were given: 
   - Strings
   - Integers outside the scope of the board 
   - Same integers were repeated twice 

![ErrorMessages](https://user-images.githubusercontent.com/116716786/225663312-9d801831-8cbd-48b2-8c59-c9a4966fa32d.png)

### Validator Testing
The code has been passed through the <a href=" https://pep8ci.herokuapp.com/" target="_blank">CI PEP8 Python Validator</a>.

![PythonLinter](https://user-images.githubusercontent.com/116716786/225642535-33e440d7-2bc3-45f5-a464-cb943fd0fe10.png)
## Deployment
This site was deployed using Code Institute’s mock terminal for Heroku. The steps for deployment are as follows:
- Fork or clone this repository 
- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository 
- Click on Deploy
#### Cloning
To create a clone of the repository within your local development environment which makes it easier to fix merge conflicts, add or remove files, and push larger commits, follow these steps:
- Log in to GitHub, access the specific GitHub Repository [Combat of Battleship](https://github.com/FarehaSi/Battleship)
- Above the file list on the repository page locate and click the 'Code' button (beside the 'Add file' button)
- Copy the provided link depending on your desired option for either 'HTTPS', 'SSH key' or 'GitHub CLI.
- Open Git Bash and change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the specific URL you copied in Step 3.
#### Forking
Forking enables a third party to create a copy of the repository in order to view and/or make changes without affecting the original. To Fork this repositary:
- Navigate to GitHub project repositary [Combat of Battleship](https://github.com/FarehaSi/Battleship)
- In the right hand corner see the "Fork" section and click on it.
- Select an owner for the forked repository.
- Click Create fork button.
## Credits
The following have been instrumental in helping me build this project:
- <a href=" https://www.youtube.com/@KnowledgeMavens" target="_blank">Knowledge Maven’s</a> YouTube videos explaining how to build a battleship game in Python.
- My mentor Akshat Garg for encouraging me to think outside the box and choose a single input method for better user experience.
