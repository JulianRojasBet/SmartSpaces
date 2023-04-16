import { ChangeEvent } from "react";

type InputProps = {
  value: string;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
};

export function Input({ value, onChange }: InputProps) {
  return (
    <input
      type="text"
      placeholder="Your place's post url"
      className="input input-bordered input-primary w-full mx-2 my-4"
      value={value}
      onChange={onChange}
    />
  );
}
