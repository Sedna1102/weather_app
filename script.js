async function getWeather() {
  const city = document.getElementById("city").value.trim();
  const apiKey = "39701159c3ab0a00dce28e210f95886d";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    if (data.cod !== 200) {
      throw new Error(data.message);
    }

    const cityName = data.name;
    const temp = data.main.temp;
    const condition = data.weather[0].main;
    const iconCode = data.weather[0].icon;
    const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;

    // Use user's local time
    const dateTime = new Date().toLocaleString("en-IN", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit"
    });

    document.getElementById("city-name").textContent = cityName;
    document.getElementById("temperature").textContent = `${temp} °C`;
    document.getElementById("condition").textContent = condition;
    document.getElementById("icon").src = iconUrl;
    document.getElementById("date-time").textContent = dateTime;
  } catch (error) {
    alert("City not found. Please try again.");
  }
}
