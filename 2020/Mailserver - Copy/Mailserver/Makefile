CC = g++
CFLAGS = -g -O2
CFLAGS_EXTRA = -lpthreaD
BIN_FILE = xsmtP
OBJ_FILES = module_mail.o module_user.o xsmtp.o
SRC_FILES = module_mail.cpp module_user.cpp xsmtp.cpp

all: $(BIN_FILE)
$(BIN_FILE): $(OBJ_FILES) xsmtp.cpp
	$(CC) $(CFLAGS) $(OBJ_FILES) -o $(BIN_FILE) $(CFLAGS_EXTRA)
$(OBJ_FILES):
	$(CC) $(CFLAGS) -c $(SRC_FILES)

clean:
	rm $(OBJ_FILES) $(BIN_FILE)
