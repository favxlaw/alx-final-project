import axios from "axios";

const base_url = process.env.SERVER_SIDE_URL;

export const privateRequest = axios.create({
  baseURL: base_url,
  headers: { "Content-Type": "application/json" },
  withCredentials: true,
});

export const api = axios.create({
  baseURL: base_url,
});

export default api;
