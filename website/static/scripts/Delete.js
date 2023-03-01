function deleteNote(noteId, userId) {
    fetch("/smazzpravu", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = `/`; 
    });
  }

function deleteProgrammer(userId) {
    fetch("/smazprogramatora", {
      method: "POST",
      body: JSON.stringify({ userId: userId }),
    }).then((_res) => {
      window.location.href = "/pridejprogramatora"; 
    });
  }
