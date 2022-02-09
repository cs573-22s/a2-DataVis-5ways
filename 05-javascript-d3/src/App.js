import { scaleLinear, schemeCategory10 } from "d3";
import { useEffect, useState } from "react";
import "./App.css";
import { loadData } from "./request";

function App() {
  const width = 1200;
  const height = 600;

  const contentWidth = width - 400;
  const contentHeight = height - 100;
  const legendWidth = 300;

  const [data, setData] = useState([]);

  const [mpgRange, setMpgRange] = useState([0, 0, 0]);
  const [weightRange, setWeightRange] = useState([0, 0, 0]);

  const [activeManufacturer, setActiveManufacturer] = useState();

  useEffect(() => {
    const load = async () => {
      const d = await loadData();
      const c = d.filter((x) => x.MPG !== "NA");
      setData(c);
      let mpgLow = d[0].MPG;
      let mpgHigh = d[0].MPG;
      let weightHigh = d[0].Weight;
      let weightLow = d[0].Weight;
      c.forEach((row) => {
        if (row.MPG < mpgLow) {
          mpgLow = row.MPG;
        } else if (row.MPG > mpgHigh) {
          mpgHigh = row.MPG;
        }
        if (row.Weight < weightLow) {
          weightLow = row.Weight;
        } else if (row.Weight > weightHigh) {
          weightHigh = row.Weight;
        }
      });
      setMpgRange([+mpgLow, +mpgHigh, +mpgHigh - +mpgLow]);
      setWeightRange([+weightLow, +weightHigh, +weightHigh - +weightLow]);
    };
    load();
  }, []);

  const xScale = scaleLinear()
    .domain([
      weightRange[0] - weightRange[2] / 20,
      +weightRange[1] + weightRange[2] / 20,
    ])
    .range([0, contentWidth]);

  const yScale = scaleLinear()
    .domain([mpgRange[0] - mpgRange[2] / 20, +mpgRange[1] + mpgRange[2] / 20])
    .range([contentHeight, 0]);

  const sizeScale = scaleLinear()
    .domain([weightRange[0], +weightRange[1]])
    .range([5, 15]);

  const manufacturers = Array.from(
    data.reduce((s, c) => {
      s.add(c.Manufacturer);
      return s;
    }, new Set())
  ).sort();

  return (
    <div className="App">
      <h1>D3 with React</h1>
      <div>
        <svg className="viz-container" width={width} height={height}>
          <g
            transform={`translate(${
              width - contentWidth - 50 - legendWidth
            }, 50)`}
          >
            {/* background */}
            <rect width={contentWidth} height={contentHeight} fill="#f0f0f0" />
            {/* xScale */}
            {xScale.ticks().map((t) => {
              const x = xScale(t);
              return (
                <g key={t} transform={`translate(${x}, 0)`}>
                  <text
                    className="scale-text"
                    y={contentHeight + 5}
                    textAnchor="middle"
                    dy="1.2em"
                  >
                    {t}
                  </text>
                  <line
                    y1={0}
                    y2={contentHeight}
                    x1={0}
                    x2={0}
                    stroke="#fff"
                    strokeWidth={2}
                  />
                  <line
                    y1={contentHeight}
                    y2={contentHeight + 5}
                    x1={0}
                    x2={0}
                    stroke="#000"
                    strokeWidth={2}
                  />
                </g>
              );
            })}
            <text
              className="axis-name"
              x={contentWidth / 2}
              y={contentHeight + 40}
              textAnchor="middle"
            >
              Weight
            </text>

            {/* yScale */}
            {yScale.ticks().map((t) => {
              const y = yScale(t);
              return (
                <g key={t} transform={`translate(0, ${y})`}>
                  <text
                    className="scale-text"
                    x={-10}
                    textAnchor="end"
                    dy="0.4em"
                  >
                    {t}
                  </text>
                  <line
                    y1={0}
                    y2={0}
                    x1={0}
                    x2={contentWidth}
                    stroke="#fff"
                    strokeWidth={2}
                  />
                  <line
                    y1={0}
                    y2={0}
                    x1={-5}
                    x2={0}
                    stroke="#000"
                    strokeWidth={2}
                  />
                </g>
              );
            })}
            <text
              className="axis-name"
              x={-contentHeight / 2}
              y={-30}
              transform="rotate(-90)"
              textAnchor="middle"
            >
              MPG
            </text>

            {/* marks */}
            {data.map((d) => {
              const c = activeManufacturer && activeManufacturer !== d.Manufacturer ? 'mark mark--hide' : 'mark';
              return (
                <g key={d[""]}>
                  <circle
                    className={c}
                    cx={xScale(d.Weight)}
                    cy={yScale(d.MPG)}
                    r={sizeScale(d.Weight)}
                    fill={
                      schemeCategory10[manufacturers.indexOf(d.Manufacturer)]
                    }
                  />
                </g>
              );
            })}
          </g>

          {/* legends */}
          <g transform={`translate(${width - legendWidth}, 50)`}>
            <text dy="0.35em" y={-30}>
              Manufacturers
            </text>

            {manufacturers.map((manufacturer, idx) => {
              return (
                <g key={manufacturer} transform={`translate(0, ${idx * 25})`}>
                  <circle
                    cx={0}
                    cy={0}
                    r={8}
                    opacity={0.5}
                    fill={schemeCategory10[manufacturers.indexOf(manufacturer)]}
                    onMouseEnter={() => {
                      setActiveManufacturer(manufacturer);
                    }}
                    onMouseLeave={() => {
                      setActiveManufacturer(null);
                    }}
                  />
                  <text x={15} dy="0.35em">
                    {manufacturer}
                  </text>
                </g>
              );
            })}
          </g>
          <g transform={`translate(${width - legendWidth}, 250)`}>
            <text dy="0.35em" y={-30}>
              Weight
            </text>

            {sizeScale.ticks(3).map((size, idx) => {
              return (
                <g key={size} transform={`translate(0, ${idx * 25})`}>
                  <circle
                    cx={0}
                    cy={0}
                    r={sizeScale(size)}
                    opacity={0.5}
                    fill="#000"
                  />
                  <text x={15} dy="0.35em">
                    {size}
                  </text>
                </g>
              );
            })}
          </g>
        </svg>
      </div>
    </div>
  );
}

export default App;
