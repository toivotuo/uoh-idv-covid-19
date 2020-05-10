import altair
import folium


def make_marker(df, country, lat, lon, dataset):

    cc = altair.Chart(df).mark_bar().encode(
        x='dateRep',
        y=dataset,
    )

    marker = folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(max_width=400).add_child(
            folium.VegaLite(cc.to_json(), width=400, height=250))
    )

    return marker
