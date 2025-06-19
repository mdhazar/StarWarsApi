from flask import Blueprint, render_template_string

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return """
    <h1>Star Wars REST API</h1>
    <ul>
        <li><a href="/api/characters">List All Characters</a></li>
        <li><a href="/api/characters/names">Character Names</a></li>
        <li><a href="/api/characters/affiliations">Character Affiliations</a></li>
        <li><a href="/api/characters/species">Character Species</a></li>
        <li><a href="/api/characters/homeworld">Character Homeworlds</a></li>
        <li><a href="/api/characters/id/6853bc03861f983d0b17f210">Get Character by ID (example: 6853bc03861f983d0b17f210)</a></li>
        <li><a href="/api/characters/Palpatine">Get Character by Name (example: Palpatine)</a></li>
    </ul>
    <h2>Update Character (Patch)</h2>
    <form onsubmit="event.preventDefault(); 
    const id = this.characterId.value;
    fetch('/api/characters/id/' + id, {
        method: 'PATCH',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
        name: this.name.value,
        affiliation: this.affiliation.value
        })
    })
    .then(res => res.json())
    .then(data => alert(JSON.stringify(data)))
    .catch(err => alert('Error: ' + err));
    ">
    <input name="characterId" placeholder="Character ID" required />
    <input name="name" placeholder="New Name" required />
    <input name="affiliation" placeholder="New Affiliation" required />
    <button type="submit">Update Character</button>
    </form>
    <h2>Delete Character by Name (DELETE)</h2>
    <form onsubmit="event.preventDefault();
    const name = this.characterName.value;
    fetch('/api/characters/' + name, {
        method: 'DELETE'
    })
    .then(res => {
        if (res.status === 204) {
        alert('Character deleted successfully');
        } else {
        return res.json().then(data => alert(JSON.stringify(data)));
        }
    })
    .catch(err => alert('Error: ' + err));
    ">
    <input name="characterName" placeholder="Character Name" required />
    <button type="submit">Delete Character</button>
    </form>
    
    </form>
    <h2>Create New Character (POST)</h2>
    <form id="create-character-form" onsubmit="event.preventDefault();
      const form = this;
      const data = {
        name: form.name.value,
        affiliation: form.affiliation.value,
        homeworld: form.homeworld.value,
        species: form.species.value,
        image: form.image.value || null
      };
      fetch('/api/characters', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })
      .then(res => res.json())
      .then(data => alert(JSON.stringify(data)))
      .catch(err => alert('Error: ' + err));
    ">
      <input name="name" placeholder="Name" required /><br />
      <input name="affiliation" placeholder="Affiliation" required /><br />
      <input name="homeworld" placeholder="Homeworld" required /><br />
      <input name="species" placeholder="Species" required /><br />
      <input name="image" placeholder="Image URL (optional)" /><br />
      <button type="submit">Create Character</button>
    </form>
    <h2>Delete All Characters (DELETE)</h2>
    <form onsubmit="event.preventDefault();
    if (confirm('Are you sure you want to delete all characters?')) {
        fetch('/api/characters', {
            method: 'DELETE'
        })
        .then(res => {
            if (res.status === 200) {
            alert('All characters deleted successfully');
            } else {
            return res.json().then(data => alert(JSON.stringify(data)));
            }
        })
        .catch(err => alert('Error: ' + err));
    }
    ">
    <button type="submit">Delete All Characters</button>
    """
