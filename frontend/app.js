let map;
lucide.createIcons();

document.addEventListener('DOMContentLoaded', () => {
  map = L.map('map').setView([28.62, 77.20], 11);
  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png').addTo(map);

  loadUnderpasses();

  document.getElementById('sim-rain').addEventListener('input', (e) => {
    document.getElementById('val-rain').innerText = `${e.target.value} mm/h`;
  });

  document.getElementById('btn-run-sim').addEventListener('click', async () => {
    const rain = document.getElementById('sim-rain').value;
    try {
      const res = await fetch(`/api/flood/simulate?rain_mm_h=${rain}`);
      const data = await res.json();
      document.getElementById('sim-text').innerText = `Total Inflow: ${data.cumulative_stormwater_inflow_m3_s} m³/s | ${data.submerged_underpasses} underpasses at risk.`;
      document.getElementById('kpi-submerged').innerText = `${data.submerged_underpasses} / ${data.total_monitored}`;
    } catch (e) {
      console.log(e);
    }
  });

  document.getElementById('btn-calc-rwh').addEventListener('click', async () => {
    const r = document.getElementById('rwh-roof').value;
    try {
      const res = await fetch(`/api/water/rwh?roof_sqm=${r}`);
      const data = await res.json();
      document.getElementById('rwh-out').innerText = `Harvest Potential: ${data.harvestable_volume_liters_year.toLocaleString()} Liters/year (${data.family_annual_water_security_pct}% Family Annual Need)`;
    } catch (e) {
      console.log(e);
    }
  });
});

async function loadUnderpasses() {
  try {
    const res = await fetch('/api/underpasses');
    const data = await res.json();
    data.nodes.forEach(n => {
      let color = n.water_depth_cm > 50 ? '#ef4444' : n.water_depth_cm > 25 ? '#f59e0b' : '#3b82f6';
      L.circleMarker([n.latitude, n.longitude], {
        radius: 8,
        color: '#fff',
        fillColor: color,
        fillOpacity: 0.8
      }).addTo(map).bindPopup(`<b>${n.location_name}</b><br>Depth: ${n.water_depth_cm} cm<br>Status: ${n.severity}`);
    });
  } catch (e) {
    console.log(e);
  }
}
