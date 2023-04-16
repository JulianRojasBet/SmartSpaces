"use client";

import { MouseEventHandler } from "react";

type SelectProps = {
  initial: string;
  options: {
    value: string;
    label: string;
  }[];
  onSelect: MouseEventHandler<HTMLOptionElement>;
};

export function Select({ initial, options, onSelect }: SelectProps) {
  return (
    <select className="select select-bordered w-full my-4 mx-2" defaultValue="default">
      <option value="default" disabled>
        {initial}
      </option>
      {options.map(({ value, label }) => (
        <option key={value} value={value} onClick={onSelect}>
          {label}
        </option>
      ))}
    </select>
  );
}
