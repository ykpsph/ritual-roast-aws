// Invoke URL of the API Gateway stage (REST API -> prod stage).
// Replace the placeholder with your own invoke URL after deploying the API.
const API_URL = "https://<api-id>.execute-api.eu-west-2.amazonaws.com/prod";

// Add recipe
async function addRecipe(recipe) {
    console.log("Adding recipe:", recipe);
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(recipe)
        });
        const data = await response.json();
        console.log("Response status:", response.status);
        console.log("response---", response, "data---", data)
        // return await response.json();
    } catch (error) {
        console.error("Error adding recipe:", error);
    }
}


// Get recipes
async function getRecipes() {
    try {
        const response = await fetch(API_URL);
        return await response.json();
    } catch (error) {
        console.error("Error fetching recipes:", error);
    }
}

document.addEventListener("DOMContentLoaded", async () => {
  const data = await getRecipes();
  console.log("API Response:", data);

  // Parse the body (convert string → JSON array)
  const recipes = JSON.parse(data.body);  

  const tbody = document.getElementById("recipeTableBody");
  tbody.innerHTML = "";

  recipes.forEach(r => {
    const row = `
      <tr>
        <td>${r.name}</td>
        <td>${r.recipe}</td>
        <td>${r.ingredients}</td>
        <td>${typeof r.description === "object" ? r.description.main : r.description}</td>
      </tr>
    `;
    tbody.innerHTML += row;
  });
});
