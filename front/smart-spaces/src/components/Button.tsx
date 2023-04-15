import { ReactNode } from "react";

type ButtonProps = {
  children: ReactNode;
  variant?: string;
  onClick?: () => void;
};

export function Button({ children, variant = "btn-primary", onClick }: ButtonProps) {
  return (
    <button className={`btn ${variant} mx-2 my-4`} onClick={onClick}>
      {children}
    </button>
  );
}
