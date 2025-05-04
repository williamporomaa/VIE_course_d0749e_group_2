# Element View  
  * Shows current element type  
  * Shows current element attributes depending on type of element  
  * Ability to decide type of element  
  * Ability to edit attributes of element depending on type of element  
# Element List  
  * Shows all the elements and board currently in the scene  
  * Selecting an element in the list brings it up in “element view”  
  * Ability to copy and paste an element  
  * Ability to organise elements in the element list  
    * Ability to create folders and add elements to folders  
  * Ability to edit functionality of multiple elements at once  
    * Edit elements inside of folders based on folder settings (for example all pieces elements will have the flag destroyable set to 1 in the folder “pieces”)  
# ToolBar  
  * Button/menu to change in-game music (default none)  
  * Button/menu to undo/redo  
  * Button/menu to save/load project  
  * Button to run game  
  * Button/menu to add element  
  * Menu to add and modify board  
    * Ability to add a board  
    * Ability to add a tile to the board  
    * Ability to create simple grids on the board  
      * Ability to automatically fill grid with tiles  
    * Ability to remove a tile to the board  
# FileViewer  
  * Opens up filesystem to add a new png, script…  
# Grid creator  
  * Create grid of different size and shape  
    * Hexagonal/square types  
  * Remove current grid  
# Base element  
  * Selecting a element in the scene brings it up in “element view”  
  * Base element attributes need to be modifiable  
    * Flag for destroyable  
# Piece element type   
  * Pieces need to be able to be snapped onto a grid  
  * Piece attributes need to be modifiable  
    * Flag for draggable  
    * Flags for snapping (tile, edge, corner, none) **in-game snapping and tool snapping\!** (separate flag for both)  
    * Scripting for movement patterns (think chess)  
    * Flag for destroyable  
    * Flag for stackable (can move to occupied square)  
    * Move piece sound effect  
# Deck element type  
  * Deck attributes need to be modifiable  
    * Contained cards  
    * Can remove cards flag  
    * Can add cards flag  
    * Draw sound effect  
    * Shuffle allowed flag  
# Card element type  
  * Card attributes need to be modifiable  
    * Flag for flippable   
# Dice element type  
  * Dice attributes need to be modifiable  
    * Number of faces for a dice  
    * Weighted dice  
# Board   
  * Board attributes need to be modifiable  
    * Tile list  
  * Tile element (NOT a base element, but a child element to the board)  
    * Custom script for tile (Think of for example monopoly tiles)  
    * Tile attributes  
      * Position  
      * Size  
      * Connected tiles (directed connection, ie. tile 1 connect to 2 \!= 2 connect to 1\)  
  * Ability to add tile element  
  * Ability to generate simple boards (i.e tiles for a chess board and other grid based boards)
# In-game UI functionality (menus and buttons)  
  * In game button attributes  
    * Menu (optional)  
    * Pre-defined functions  
      * Adjust volume  
      * Quit game  
      * Open menu  
        * Menu to open (back button can use this also)  
      * Add element  
        * Element type  
    * Custom scripts  
    * Text  
  * In game menu attributes  
    * Button list (ATLEAST 1 back button)  
    * Text  
# Ability to add elements to the scene  
  * Game elements should be addable as images from a file system (this image then represents the object in game and in the tool ui)  
  * Game elements that are added need to be added to the element list and shown on the scene by default, game elements become “base element” by default.  
  * Game elements need to be removable from the scene  
  * Game elements need to be copyable   
# A scene to show a preview of the game and act as a place to interact with game elements  
  * Ability to select elements represented on the scene  
    * Ability to also select multiple elements on the scene   
  * Representations of added elements in the scene  
  * Representation of a grid to help construct the game  
# Global script handler  
  * Ability to add global scripts such as win conditions
