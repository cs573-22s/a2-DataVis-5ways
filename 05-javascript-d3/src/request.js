import { csv } from "d3";

export const loadData = async () => {
  return await csv("/cars-sample.csv");
};
